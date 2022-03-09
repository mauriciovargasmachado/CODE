function car (make, model, year){
    this.make = make;
    this.model = model;
    this.year = year;
  }
  var cars = [];
  for(let i = 0 ; i < 2 ; i++){
    var make = prompt("please instoduce your car brand: ");
    var model = prompt("please introduce your car model: ");
    var year = prompt("please introduce your car year");
    cars.push(new car (make, model, year));
  }
  
  for(let i = 0 ; i < cars.length ; i++){
    console.log(cars[i]);
  }