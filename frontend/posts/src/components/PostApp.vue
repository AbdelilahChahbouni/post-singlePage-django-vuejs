<template>
    <div class="container post-card">
        <h1>Posts Here</h1>
        <div class="post-body" v-for="post in posts" :key="post.id">
            <div class="post-user">
                <img src="@/assets/img.avif" alt="">
                <h2>{{post.author}}</h2>
            </div>
                
            <div class="post-content">
                    <h3 class="post-title">{{ post.title }}</h3>
                    <p class="post-text">{{post.content}}</p>
            </div>
            <div class="like-section">
                <i class="fa-regular fa-thumbs-up"><span>{{ likes.length }}</span></i> 
                <button @click="toggleCard" class="btn btn-primary">Show Users</button>   
            </div>
             <div class="post-actions">
                <a href="#"  v-if="counter==2" @click="remove_like_from_post"><i class="fa-regular fa-solid  fa-thumbs-up"></i>Like</a>
                <a href="#"  v-if="counter==1" @click="add_like_to_post"><i class="fa-regular  fa-thumbs-up"></i>Like</a>
                <div class="comments">
                    <a data-bs-toggle="collapse" @click="fetchComments('')" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
                        <i class="fa-regular fa-comment"></i>Comments <span> {{ comments.length }}</span>
                    </a>

                </div>
            </div>
            <div class="collapse" id="collapseExample" >
                <div class="card card-body " style="background-color: #999; overflow: scroll; height: 200px;" >
                    <div class="comment-content">
                        <div class="add-comment">
                            <input type="text" @keyup.enter="createComment" placeholder="add Comment" class="w-75" v-model="input_content">
                            <div class="dropdown">
                                <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Filter Comments
                                </button>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="#" @click="fetchComments('?ordering=create_at')">old</a></li>
                                    <li><a class="dropdown-item" href="#" @click="fetchComments('?ordering=-create_at')">Last</a></li>
      
                                </ul>
                            </div>
                        </div>
                        <div class="list-comments" v-for="item in comments" :key="item.id">
                            <div class="items-comment">
                                <div class="post-user">
                                    <img src="@/assets/img.avif" alt="" style="width: 40px; height: 40px;">
                                    <h2>{{item.author}}</h2>
                                </div>
                                <p>{{ item.content }}</p>
                            </div>
                           
                        </div>
                    </div>
                </div>
            </div>
            <!-- card user make like on the post -->
            <div class="like-users" >    
              <div v-if="showCard" class="card my-card" >
                    <div class="card-body " style="background-color: #999; color:#444;" v-for="user in likes" :key="user.id">
                        
                        <div class="post-user">
                            <img src="@/assets/img.avif" alt="" style="width: 30px; height: 30px;">
                            <h2>{{ user.user}}</h2>
                        </div>
                        
                    </div>
                </div>
            </div>
            
        </div>
    </div>



   
</template>


<script>
    import '@/assets/styles/style.css'
    import axios from 'axios';
    const authToken ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NTg2Nzk0LCJpYXQiOjE3MDc1MDAzOTQsImp0aSI6IjJiNmJkZWRmMzJkYzQ4OGFhYTk5Njc3MzBlZmI2NjNmIiwidXNlcl9pZCI6MX0.GEKCP9whhtPsK-q8fKW3oSIZwhAX6KCIvwDdA5foyzQ';
    
    export default {
        name : 'post-app',
        data() {
            return {
      showCard: false,
      posts : [],
      comments : [],
      likes : [],
      input_content : "",
      counter : 1,
      status : "",
    };
  },
  mounted() {
    
    axios.get('http://localhost:8000/post/api/list')
      .then(response => {
        this.posts = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
      this.getLikes();
      this.fetchComments("")
  },
  methods: {
   fetchComments(value){
    axios.get('http://localhost:8000/post/api/comment/list/1'+value)
      .then(response => {
        this.comments = response.data;
        console.log(this.comments)
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      })

   },
   getLikes(){
    axios.get('http://localhost:8000/post/api/like/list/1')
      .then(response => {
        this.likes = response.data;
        console.log(this.comments)
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      })
   },
   // add like to current post
   add_like_to_post(){
      const likeData ={
        post : 1
      };
      axios.post("http://localhost:8000/post/api/like/add" ,likeData ,{
        headers : {
          'Authorization': `Bearer ${authToken}`, // Include token in the request headers
          'Content-Type': 'application/json', // Set content type if required
        },
      }).then(response => {
        this.status = response.data;
        this.counter++ ;
        this.getLikes()
      })
      .catch(error => {
      console.error('Error creating comment:', error);
      });
   },
   remove_like_from_post(){
      
      axios.delete("http://localhost:8000/post/api/like/delete/1",{
        headers : {
          'Authorization': `Bearer ${authToken}`, // Include token in the request headers
          'Content-Type': 'application/json', // Set content type if required
        },
      }).then(response => {
        // console.log('Response from server:', response.data['message']);
        this.status = response.data["message"]
        this.counter--;
        this.getLikes()
      })
      .catch(error => {
      console.error('Error creating comment:', error);
      });
   },

   toggleCard() {
     this.showCard = !this.showCard; 
   },
   // create comment
   createComment() {
    const commentData = {
        content: this.input_content,
        post : 1,
  
      };
    axios.post('http://localhost:8000/post/api/comment/create', commentData, {
  headers: {
    'Authorization': `Bearer ${authToken}`, // Include token in the request headers
    'Content-Type': 'application/json', // Set content type if required
  },
  
})
.then(response => {
  console.log('Comment created successfully:', response.data);
  this.fetchComments("?ordering=-create_at");
  this.input_content= "";
})
.catch(error => {
  console.error('Error creating comment:', error);
});
}
  },
 }



  










</script>







