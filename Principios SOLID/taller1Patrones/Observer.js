// --- Observador.js (Clase base) ---
class Observador {
  constructor(sujeto) {
      this.sujeto = sujeto;
      this.sujeto.agregar(this);
  }
  actualizar() {}
}

// --- Subject.js ---
class Subject {
  constructor() {
      this.observadores = [];
      this.estado = 0;
  }

  getEstado() {
      return this.estado;
  }

  setEstado(estado) {
      this.estado = estado;
      this.notificarTodosObservadores();
  }

  agregar(observador) {
      this.observadores.push(observador);
  }

  notificarTodosObservadores() {
      this.observadores.forEach(obs => obs.actualizar());
  }
}

// --- SolObservador.js ---
class SolObservador extends Observador {
  constructor(sujeto) {
      super(sujeto);
      this.valorCambio = 3.25;
  }

  actualizar() {
      console.log(`PEN: ${this.sujeto.getEstado() * this.valorCambio}`);
  }
}

// --- PesoMXObservador.js ---
class PesoMXObservador extends Observador {
  constructor(sujeto) {
      super(sujeto);
      this.valorCambio = 19.07;
  }

  actualizar() {
      console.log(`MX: ${this.sujeto.getEstado() * this.valorCambio}`);
  }
}

// --- PesoARGObservador.js ---
class PesoARGObservador extends Observador {
  constructor(sujeto) {
      super(sujeto);
      this.valorCambio = 29.86;
  }

  actualizar() {
      console.log(`ARG: ${this.sujeto.getEstado() * this.valorCambio}`);
  }
}

// --- App.js ---
(function() {
  const subject = new Subject();

  new SolObservador(subject);
  new PesoARGObservador(subject);
  new PesoMXObservador(subject);

  console.log("Si desea cambiar 10 dólares obtendrá:");
  subject.setEstado(10);
  console.log("-----------------");
  console.log("Si desea cambiar 100 dólares obtendrá:");
  subject.setEstado(100);
})();
