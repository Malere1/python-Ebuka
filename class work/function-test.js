const { add } = require('./function')

test("test addition of two positive number",()=> {
   let firstNumber = 82;
   let SecondNumber= 18; 

   expect(add(firstNumber,SecondNumber)).toBe(110)
   
   
   
   })
