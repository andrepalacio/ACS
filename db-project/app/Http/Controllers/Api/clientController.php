<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Client;
use Illuminate\Support\Facades\Validator;

class clientController extends Controller
{

    public function index()
    {
        $clients = Client::all();
        if ($clients->isEmpty()) {
            return response()->json(['message' => 'No clients found'], 404);
        }
        return response()->json($clients, 200);
    }

    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'name' => 'required',
            'surname' => 'required',
            'email' => 'required|email|unique:clients',
            'age' => 'required|numeric'
        ]);

        if ($validator->fails()) {
            $data = [
                'message' => 'Validation data failed, wrong data input',
                'errors' => $validator->errors()
            ];
            return response()->json($data, 400);
        }

        $client = Client::create([
            'name' => $request->name,
            'surname' => $request->surname,
            'email' => $request->email,
            'age' => $request->age,
        ]);
        
        if (!$client) {
            return response()->json(['message' => 'Client could not be created'], 500);
        }
        return response()->json($client, 201);
    }

    public function show(string $id)
    {
        $client = Client::find($id);
        if (!$client) {
            return response()->json(['message' => 'Client not found'], 404);
        }
        return response()->json($client, 200);
    }

    public function update(Request $request, string $id)
    {
        $client = Client::find($id);
        if (!$client) {
            return response()->json(['message' => 'Client not found'], 404);
        }

        $validator = Validator::make($request->all(), [
            'name' => 'string',
            'surname' => 'string',
            'age' => 'numeric'
        ]);

        if ($validator->fails()) {
            $data = [
                'message' => 'Validation data failed, wrong data input',
                'errors' => $validator->errors()
            ];
            return response()->json($data, 400);
        }

        if ($request->has('name')) {
            $client->name = $request->name;
        }
        if ($request->has('surname')) {
            $client->surname = $request->surname;
        }
        if ($request->has('age')) {
            $client->age = $request->age;
        }
        $client->save();

        return response()->json($client, 200);
    }

    public function destroy(string $id)
    {
        $client = Client::find($id);
        if (!$client) {
            return response()->json(['message' => 'Client not found'], 404);
        }
        $client->delete();
        return response()->json(['message' => 'Client deleted'], 200);
    }
}
