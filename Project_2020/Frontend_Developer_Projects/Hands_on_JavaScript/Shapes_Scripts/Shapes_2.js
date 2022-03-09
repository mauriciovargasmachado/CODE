



// Square

console.group("Square");


function square_perimeter(side){
    return side *4;
}

square_perimeter ();

function square_area(side){
    return side *side;
}

square_area ();


console.groupEnd();

// Triangle

console.group("Triangles");


function triangle_perimeter(base,side_1,side_2){
    return parseInt(base) + parseInt(side_1) + parseInt(side_2);
}

triangle_perimeter ();

function triangle_area(base,height){
    return (base * height)/2;
}


triangle_area ();


console.groupEnd()

// Circle


console.group("Circle");

const pi = Math.PI;

function circle_perimeter(diameter){
    return (diameter*pi);
}

function radius(diameter){
    return diameter/2;
}

circle_perimeter ();

function circle_area(radius){
    return (radius*radius*pi);

}
console.groupEnd()

// integration with HTML

function buttonA(){
    const input = document.getElementById("input_square");
    const value = input.value;

    const s_perimeter =square_perimeter(value);
    alert(s_perimeter);
}

function buttonB(){
    const input = document.getElementById("input_square");
    const value = input.value;

    const s_area =square_area(value);
    alert(s_area);
}

//integration HTML triangle

function buttonC(){
    const input_1 = document.getElementById("input_triangle_1");
    const input_2 = document.getElementById("input_triangle_2"); 
    const input_3 = document.getElementById("input_triangle_3");
    
    const base = input_1.value;
    const side_1 = input_2.value;
    const side_2 = input_3.value;
    

    const t_perimeter =triangle_perimeter(base,side_1,side_2);
    alert(t_perimeter);

    }

function buttonD(){
    const input_1 = document.getElementById("input_triangle_1");
    const input_4 = document.getElementById("triangle_height");
    const value_1 = input_1.value;
    const value_4 = input_4.value;

    const t_area =triangle_area(value_1,value_4);
    alert(t_area);
}


//integration HTML circle

function buttonE(){
    const input_5 = document.getElementById("input_circle");
    
    const value_5 = input_5.value;
       
    const c_perimeter =circle_perimeter(value_5);
    alert(c_perimeter);

    }

function buttonF(){
    const input_5 = document.getElementById("input_circle");
    
    const value_5 = input_5.value;
       
    const c_area =circle_area(value_5);
    alert(c_area);
    
}
