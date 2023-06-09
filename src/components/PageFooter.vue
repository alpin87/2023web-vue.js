<template>
    <footer>
    <hr>
    <div class="image-container">
        <a href="https://www.instagram.com/alpen_1/" target="_blank">
            <img src="@/assets/instagram.png" alt="image description" class="footer-image"/>
        </a>
        <!-- Add more images as needed -->
        <a href="https://github.com/alpin87" target="_blank">
            <img src="@/assets/github.png" alt="image description" class="footer-image"/>
        </a>
        <a href="https://www.facebook.com/profile.php?id=100004923222265" target="_blank">
            <img src="@/assets/face.png" alt="image description" class="footer-image"/>
        </a>
    </div>
    <div class="copyright">
        Developer : Baek Seung Min <br>
        © 2023 BSM. All rights reserved.
    </div>
    </footer>
</template>

<script>
</script>

<style>
.footer-image {
    margin-top:30px;
    margin-right: 30px;
    width : 50px;
    height : 50px;
}

.image-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.copyright {
    text-align: center;
    margin-top: 20px;
    margin-right:45px;
}
</style>
