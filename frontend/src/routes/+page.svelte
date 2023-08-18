<script lang="ts">
	import { enhance } from '$app/forms';
	import {
		Card,
		Label,
		Input,
		Button,
		Fileupload,
		Blockquote,
		Timeline,
		TimelineItem,
		Footer,
		FooterCopyright,
		FooterLinkGroup,
		FooterBrand,
		FooterLink
	} from 'flowbite-svelte';

	let value: any;
</script>

<body class=" leading-relaxed tracking-wide flex flex-col">
	<!--Nav-->
	<nav id="header" class="w-full z-30 top-0 text-white fixed bg-white shadow-sm">
		<div
			class="w-full container mx-auto flex flex-wrap items-center justify-between mt-0 px-2 py-2 lg:py-3"
		>
			<div class=" pl-4 flex items-center text-black">
				<FooterBrand href="#" src="/logo1.png" alt="청바지몰" />
				<a class="no-underline hover:no-underline font-bold text-2xl lg:text-3xl" href="/">
					<path d="M13 8V0L8.11 5.87 3 12h4v8L17 8h-4z" />
					
				</a>
			</div>
			<div class="hidden w-full md:block md:w-auto" id="navbar-default">
				<div class="flex md:order-2">
					<button
						type="button"
						class="flex text-white bg-pink-400 hover:bg-white hover:text-black focus:ring-4 focus:outline-none focus:ring-blue-300 font-large font-bold rounded-lg text-sm px-4 py-2 text-center mr-2 md:mr-5"
						><a href="/login">로그인</a></button
					>
				</div>
			</div>
		</div>
	</nav>
	<!-- container mx-auto h-screen bg-pink-700 -->
	<div class="h-1/2 mt-7 lg:mt-9 bg-img-top bg-pink-800">
		<!-- bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/conference.jpg')] -->
		<!-- bg-gradient-to-r from-gray-300 via-gray-500 to-gray-700 -->
		<!-- <div
			class="w-full h-3 bg-gradient-to-r from-white via-gray-500 to-gray-700 animate-gradient-shift"
		/> -->
		<div class="text-center px-3 lg:px-10 p-20 mt-10">
			<h1
				class="my-4 text-4xl md:text-3xl lg:text-5xl text-pink font-extrabold leading-tight pb-5"
			>
				청.바.지
			</h1>
			<p class="leading-normal text-black-400 text-base md:text-4xl lg:text-3xl mb-8 font-extrabold">
				청춘을 바로 지금<br>
				고령자를 위한 쇼핑몰
			</p>

			<button
				class="text-xl mx-auto lg:mx-0 border p-10 border-pink bg-white hover:font-extrabold rounded-lg rounded my-2 md:my-6 py-4 px-8 shadow-lg w-48"
			>
				<a href="/login"> 시작하기 </a>
			</button>
		</div>
		<!-- <div
			class="w-full h-3 bg-gradient-to-r from-gray-700 via-gray-500 to-white animate-gradient-shift"
		/> -->
		<div class="flex items-center w-full mx-auto content-end md-block">
			<div
				class="browser-mockup flex flex-1 m-6 md:px-0 md:m-12 bg-white w-1/2 rounded shadow-xl"
			/>
		</div>
	</div>
</body>

	<!--Footer-->
	<!-- <footer class="flex bg-white rounded-lg shadow m-4 dark:bg-gray-800">
    <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
      <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <a href="#" class="hover:underline">청바지몰</a>. All Rights Reserved.
    </span>
    <ul class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6 ">About</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Licensing</a>
        </li>
        <li>
            <a href="#" class="hover:underline">Contact</a>
        </li>
    </ul>
    </div>
</footer> -->

	


<style>
	.bg-img-top {
		background: 
			url('/logo1.png');

		/* background-image: url('/bg.jpg'); */
		background-repeat: no-repeat;
		background-size: cover;
	}

	.bg-img-bottom {
		background: 
					/* You can uncomment and adjust other gradient stops if needed */
			
			url('/logo1.png');

		/* background-image: url('/bg.jpg'); */
		background-repeat: no-repeat;
		background-size: cover;
	}

	.scroll-down {
		position: absolute;
		left: 50%;
		bottom: 10px;
		display: block;
		text-align: center;
		font-size: 20px;
		z-index: 100;
		text-decoration: none;
		text-shadow: 0;
		width: 13px;
		height: 13px;
		border-bottom: 2px solid #000; /* 이 부분을 검은색으로 변경 */
		border-right: 2px solid #000; /* 이 부분을 검은색으로 변경 */
		z-index: 9;
		left: 50%;
		-webkit-transform: translate(-50%, 0%) rotate(45deg);
		-moz-transform: translate(-50%, 0%) rotate(45deg);
		transform: translate(-50%, 0%) rotate(45deg);
		-webkit-animation: fade_move_down 4s ease-in-out infinite;
		-moz-animation: fade_move_down 4s ease-in-out infinite;
		animation: fade_move_down 4s ease-in-out infinite;
	}

	/*animated scroll arrow animation*/
	@-webkit-keyframes fade_move_down {
		0% {
			-webkit-transform: translate(0, -10px) rotate(45deg);
			opacity: 0;
		}
		50% {
			opacity: 1;
		}
		100% {
			-webkit-transform: translate(0, 10px) rotate(45deg);
			opacity: 0;
		}
	}
	@-moz-keyframes fade_move_down {
		0% {
			-moz-transform: translate(0, -10px) rotate(45deg);
			opacity: 0;
		}
		50% {
			opacity: 1;
		}
		100% {
			-moz-transform: translate(0, 10px) rotate(45deg);
			opacity: 0;
		}
	}
	@keyframes fade_move_down {
		0% {
			transform: translate(0, -10px) rotate(45deg);
			opacity: 0;
		}
		50% {
			opacity: 1;
		}
		100% {
			transform: translate(0, 10px) rotate(45deg);
			opacity: 0;
		}
	}
</style>
