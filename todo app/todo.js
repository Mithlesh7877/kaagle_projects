// but=document.getElementById('b');
// but.addEventListener('click',function(){
//     document.getElementById("p").textContent = "Paragraph changed!";
// });
var ffield=document.querySelector('form');
var list=document.querySelector('ul');
var button=document.getElementById('b')
var input=document.getElementById('to');
var array=localStorage.getItem('todos')?JSON.parse(localStorage.getItem('todos')):[];
localStorage.setItem('todos',JSON.stringify(array));
var storage=JSON.parse(localStorage.getItem('todos'));


ffield.addEventListener('submit',function (e){
    e.preventDefault();
    // console.log('submit');
    array.push(input.value);
    localStorage.setItem('todos',JSON.stringify(array));
    todo(input.value);
    input.value='';

});

var todo =  function(text){
    var tod=document.createElement('li');
    tod.textContent=text;
    list.appendChild(tod);
}

for (var i=0;i<storage.length;i++){
    todo(storage[i]);
}

button.addEventListener('click',function(){
    localStorage.clear();
    while(list.firstChild){
        list.removeChild(list.firstChild)
    }
});