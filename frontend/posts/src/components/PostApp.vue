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
    import '@/assets/styles/style.css'
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







