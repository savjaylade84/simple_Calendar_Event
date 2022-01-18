
//this will change text to datetime type of input
const run = () => {
    const toDate = document.querySelector('.toDate')
    const fromDate = document.querySelector('.fromDate')
    const event = document.querySelector('.event')
    const Months = document.querySelector('.Months')
    
        toDate.addEventListener('focus',()=>{
            toDate.type = "datetime-local";
        });
        fromDate.addEventListener('focus',()=>{
            fromDate.type = "datetime-local";
        });
       
}

run()