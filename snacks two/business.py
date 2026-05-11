function maxFrequency(arr) {
    let freq = {};

    for (let num of arr) {
        if (freq[number]) {
            freq[number]++;
        } else {
            freq[number] = 1;
        }
    }

   
    let max = 0;
    for (let key in freq) {
        if (freq[key] > max) {
            max = freq[key];
        }
    }

    return max;
}


let input1 = [1, 2, 2, 2, 3];
console.log(maxFrequency(input1));

let input2 = [1, 5, 5, 6, 4];
console.log(maxFrequency(input2));
