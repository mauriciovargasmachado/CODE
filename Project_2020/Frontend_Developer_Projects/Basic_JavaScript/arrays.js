var fruits  = ["platain","cherry","apple","orange","pinaple"];
console.log(fruits);

var studients  = ["Jhon","Marc","Joel","David","James"];

function say_hi_student(studient){
    console.log("Hi, "+ studient);
}

for (var i = 0; i < studients.length; i++ ){
    say_hi_student(studients[i]);
}

for(var studient of studients){
    say_hi_student(studient)
}

