var updateBtns = document.getElementsByClassName('update-download')

for (i=0;i<updateBtns.length;++i) {
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action 
        console.log('productId',productId,'action',action)
        console.log('USER: ',user)
        if(user === 'AnonymousUser' ){
            console.log('Not logged in')
            
        }else{
            updateDownload(productId,action)
        }
    })
}

function updateDownload(productId,action) {
    console.log('success add')
    var url ="/update_download/"
    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productId':productId,'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:',data)
        location.reload()
    })
}