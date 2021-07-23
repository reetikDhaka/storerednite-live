console.log('working')
let likebtn = document.getElementById('like');

likebtn.addEventListener('click', function(){
     username = this.dataset.username;
     action = this.dataset.action
     console.log(username, action)
     if (username =='AnonymousUser'){
         alert('you are not logged in');
     }
     //now api function
     let url = '/mytest/jsonrequest';
     fetch(url,{
         method:'POST',
         headers:{
             'Content-Type':'application/json',
             'X-CSRFToken': csrftoken,
         },
         body: JSON.stringify({'username': username, 'action': action})
     })
     .then((response)=> {
           return response.json()
     })
     .then((data)=>{
         console.log(data)
     })
})