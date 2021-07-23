let cartbtns = document.getElementsByClassName('update-cart');
console.log('hello');
//let cartbtns = document.querySelector('.update-cart');
for(var i=0; i<cartbtns.length;i++){
    cartbtns[i].addEventListener('click', function(){
       productId = this.dataset.product;
       action = this.dataset.action;
       console.log(productId)
       if (user == 'AnonymousUser')
       {
       addCookieItem(productId,action)
       
        }
       else {
          
        updateCart(productId,action)
        
       }
    }
    );
}
//for logged in user
function updateCart(productId,action){
 
   console.log('api workingdfsdf');
   let url = '/update-cart';
   fetch(url,{
       method:'POST',
       headers:{
         'Content-Type': 'application/json',
         'X-CSRFToken': csrftoken,
       },
       body: JSON.stringify({'productId' :productId, 'action' :action})
   })
   .then((response)=> {
      return response.json()
   })
   .then((data)=>{
     document.location.reload()
   })
}

//for annoynmous user
function addCookieItem(productId,action){
   console.log('not logged in.')
   if (action == 'add'){
      if(cart[productId] == undefined){
         cart[productId] = {'quantity':1};
         console.log('creating if')
      }
      else{
         cart[productId]['quantity']+=1;
      }
     // console.log(cart)
     console.log('Cart:', cart)
   }
   if (action=='remove'){
      cart[productId]['quantity']-=1
      if (cart[productId]['quantity']<=0){
         console.log('delting item')
         delete cart[productId]
       
      }

   }

}

//
