const lateral_square = 5;
Units = " cm";
const lateral_triangle_1 = 5;
const lateral_triangle_2 = 5;
const lateral_triangle_3 = 5;
const triangle_height =5;
const radius =5;
const diameter =5;
const pi=Math.PI;


// Square
console.group("Squares");

console.log("The laterals of the square are: "+ lateral_square + Units);

const perimeter_square = lateral_square*4;

console.log("The total perimeter of the square is: "+ perimeter_square + Units);

const area_square = lateral_square*lateral_square;

console.log("The total Area of the square is: "+ area_square + Units);

console.groupEnd();

// Triangle
console.group("Triangles");

console.log("The laterals of the triangle are: "+ lateral_triangle_1 + Units + " and " + lateral_triangle_2 + Units + " and " + lateral_triangle_3 + Units);

const perimeter_triangle = lateral_triangle_1+lateral_triangle_2+lateral_triangle_3;

console.log("The total perimeter of the triangle is: "+ perimeter_triangle + Units);

const area_triangle = ((lateral_triangle_1*triangle_height)/2);

console.log("The total Area of the triangle is: "+ area_triangle + Units);
console.groupEnd()

// Circle
console.group("Circle");

console.log("The circunference of a circle is: "+ diameter *pi);

const area_circle = ((radius*radius)*pi);

console.log("The total Area of the circle is: "+ area_circle + Units);
console.groupEnd()