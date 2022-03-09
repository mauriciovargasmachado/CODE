var studients =  ["Jhon","Marc","Joel","David","James"];

function say_hi_student(studient){
    console.log("Hi, "+ studient);
}

while( studients.length>0){
    var studient = studients.shift();
    say_hi_student(studient);
}