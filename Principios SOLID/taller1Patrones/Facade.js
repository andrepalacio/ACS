// --- AvionAPI.js ---
class AvionAPI {
  buscarVuelos(fechaIda, fechaVuelta, origen, destino) {
      console.log("==============================");
      console.log(`Vuelos encontrados para ${destino} desde ${origen}`);
      console.log(`Fecha IDA: ${fechaIda} Fecha Vuelta: ${fechaVuelta}`);
      console.log("==============================");
  }
}

// --- HotelAPI.js ---
class HotelAPI {
  buscarHoteles(fechaEntrada, fechaSalida, origen, destino) {
      console.log("==============================");
      console.log("Hoteles encontrados");
      console.log(`Entrada: ${fechaEntrada} Salida: ${fechaSalida}`);
      console.log("Hotel A");
      console.log("Hotel B");
      console.log("Hotel C");
      console.log("==============================");
  }
}

// --- CheckFacade.js ---
class CheckFacade {
  constructor() {
      this.avionAPI = new AvionAPI();
      this.hotelAPI = new HotelAPI();
  }

  buscar(fechaIda, fechaVuelta, origen, destino) {
      this.avionAPI.buscarVuelos(fechaIda, fechaVuelta, origen, destino);
      this.hotelAPI.buscarHoteles(fechaIda, fechaVuelta, origen, destino);
  }
}

// --- App.js ---
(function() {
  const cliente1 = new CheckFacade();
  cliente1.buscar("02/07/2018", "08/07/2018", "Lima", "Cancún");

  const cliente2 = new CheckFacade();
  cliente2.buscar("02/07/2018", "08/07/2018", "Lima", "Quito");
})();
