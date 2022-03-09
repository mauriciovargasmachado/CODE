var things = [{title:"bike",price:"3000"},{title:"car",price:"23000"},{title:"phone",price:"1000"}
];


var selected_things = things.map(function(things){ return things.name});



var selected_things = things.filter(function(things){ return things.cost <= 5000});


var selected_things = things.find(function(things){ return things.name === "car"});

things.forEach(function(things){console.log(things.name)});

var things_cheap = things.some(function(things){return things.cost < 700});
