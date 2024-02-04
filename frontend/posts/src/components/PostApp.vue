<template>
    <div class="container post-card">
        <h1>Posts Here</h1>
        <div class="post-body">
            <div class="post-user">
                <img src="@/assets/img.avif" alt="">
                <h2>userName</h2>
            </div>
                
            <div class="post-content">
                    <h3 class="post-title">title post</h3>
                    <p class="post-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, ducimus?</p>
            </div>
            <div class="like-section">
                <i class="fa-regular fa-thumbs-up"><span>30</span></i> 
                <button @click="toggleCard" class="btn btn-primary">Show Users</button>   
            </div>
             <div class="post-actions">
                <a href="#"><i class="fa-regular fa-thumbs-up"></i>Like</a>
                <div class="comments">
                    <a data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
                        <i class="fa-regular fa-comment"></i>Comments
                    </a>

                </div>
            </div>
            <div class="collapse " id="collapseExample" >
                <div class="card card-body " style="background-color: #999;">
                    <div class="comment-content">
                        <div class="add-comment">
                            <input type="text" name="" id="" placeholder="add Comment" class="w-75">
                            <div class="dropdown">
                                <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Filter Comments
                                </button>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="#">Last</a></li>
                                    <li><a class="dropdown-item" href="#">old</a></li>
                                    <li><a class="dropdown-item" href="#">all</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="list-comments">
                            <div class="items-comment">
                                <div class="post-user">
                                    <img src="@/assets/img.avif" alt="" style="width: 40px; height: 40px;">
                                    <h2>userName</h2>
                                </div>
                                <p>Comment 1</p>
                            </div>
                           
                        </div>
                    </div>
                </div>
            </div>
            <!-- card user make like on the post -->
            <div class="like-users">    
              <div v-if="showCard" class="card my-card">
                    <div class="card-body " style="background-color: #999; color:#444;">
                        
                        <div class="post-user">
                            <img src="@/assets/img.avif" alt="" style="width: 30px; height: 30px;">
                            <h2>userName</h2>
                        </div>
                        <div class="post-user">
                            <img src="@/assets/img.avif" alt="" style="width: 30px; height: 30px;">
                            <h2>userName</h2>
                        </div>
                        
                    </div>
                </div>
            </div>
            
        </div>
    </div>



   
</template>


<script>
    export default {
        name : 'post-app',
        data() {
            return {
      showCard: false,
    };
  },
  methods: {
    toggleCard() {
      this.showCard = !this.showCard;
    },
  },







    }


</script>

<style>
    .post-card {
        background-color: #eee;
        border-radius: 5px;
        margin-top: 100px;
        display: block;
        height: 100vh;
        
}
.post-card h1 {
    color : blueviolet;
    font-size: 30px;
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
}
.post-body {
    background-color: #9999;
    width: 55%;
    margin: auto;
    padding: 10px;
    border-radius: 7px;
    position: relative;
}
.post-body .post-user {
    display: flex;
    align-items: center;
}
.post-user img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-right: 10px
}
.post-user h2 {
    font-size: 18px;
    margin-top: 10px;

}
.post-content .post-title {
    margin-top: 23px;
    font-size: 20px;
    color: #777;

}

.post-content p{
    font-size : 18px;
    line-height: 1.6;
    color: #444

}
.post-body .like-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
    border-top: 1px solid #eee;
    border-bottom: 1px solid #eee;
    padding-top: 10px;
    padding-bottom: 10px;
}
.like-section i {
    color : blue;
    margin-right: 10px;
    font-size: 20px;
}
.like-section i span {
    display: inline-block;
    margin-left: 10px;
    color: blue;
    font-size: 15px;
}
.like-section > span {
    color: blue;
}
.post-body .post-actions {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 10px ;
}

.post-actions a {
    text-decoration: none;
    color : blue;
    
}
.post-actions a i {
    font-size: 20px;
    display: inline-block;
    margin-right: 10px;
}
.comment-content .add-comment {
    display: flex;
    justify-content: space-between;
}
.comment-content .add-comment input {
    border-radius: 8px;
    color:#777;
    outline: none;
    border: none;
    padding-left: 10px;

}
.my-card {
    width: 200px;
    height: 400px;
    background-color: #999;
    color:#444
}
.like-users {
    position: absolute;
    top: 200px;
    right:-200px;
    background-color:#999 ;
    color: white;
    
}
.list-comments {
    background-color: #ccc;
    border-radius: 10px;
    margin-top: 10px;
    padding: 10px;
}
.list-comments p {
    margin-top: 15px;
    padding-left: 20px;
    color: #444;
    font-size: 18px;
}


</style>
