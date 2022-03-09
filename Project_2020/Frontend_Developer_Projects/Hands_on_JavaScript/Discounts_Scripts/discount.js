
function final_price(price, discount){

    const discount_percentage = (price*discount)/100;
    
    const discount_price = price - discount_percentage;

    return discount_price;
    
}

function push_button(){

    const A = document.getElementById("P").value;
    const B = document.getElementById("D").value;
    const discount_price = final_price(A,B);
    console.log(discount_price);

    const resultP = document.getElementById("resultP");
    resultP.innerText = "EL PRECIO FINAL ES: $" + discount_price;
}



