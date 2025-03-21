<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Api\clientController;

Route::get('/clients', [clientController::class, 'index']);

Route::get('/clients/{id}', [clientController::class, 'show']);

Route::post('/clients', [clientController::class, 'store']);

Route::put('/clients/{id}', [clientController::class, 'update']);

Route::delete('/clients/{id}', [clientController::class, 'destroy']);