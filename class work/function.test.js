const { add } = require('./function')

test("test addition of two positive number",()=> {
   let firstNumber = 82;
   let SecondNumber= 18; 

   expect(add(firstNumber,SecondNumber)).toBe(110)
   
   
  })
  
  test("test addition of two positive number and a nagative number work accurately",() =>{ 
   let firstNumber = -10;
   let SecondNumber= -5; 
    expect(add(firstNumber,SecondNumber)).toBe(-15)
    
    
    })
    test("test that substraction")
    let firstNumber =80;
    let firstNumber = 15;
     expect(substract(firstNumber,SecondNumber)).toBe(65)
     
     
     })
     
     
   test()
