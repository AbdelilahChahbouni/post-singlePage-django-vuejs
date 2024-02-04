<template>
    <!-- Start Header section -->
    <div class="mb-5">
        <nav class="navbar bg-body-tertiary fixed-top">
            <div class="container-fluid">
                <a class="navbar-brand">Post</a>
                <form class="d-flex w-50 justify-content-between" role="search" >
                    <input class="form-control me-2 w-75" type="search" placeholder="Search" aria-label="Search">
                    <div>
                        <button class="btn btn-outline-success me-2" type="submit">Log in</button>
                        <button class="btn btn-outline-success" type="submit">Sign up</button>
                    </div>
                
                </form>
            </div>
        </nav>
    </div>
    <!-- End Header Section -->
</template>

<script>
    export default {
        name : 'header-app',
        
    }



</script>