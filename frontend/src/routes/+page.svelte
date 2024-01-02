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
		FooterLink,
		GradientButton,
		P
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
						class="flex text-white bg-greenToBlue-400 hover:bg-white hover:text-black focus:ring-4 focus:outline-none focus:ring-blue-300 font-large font-bold rounded-lg text-sm px-4 py-2 text-center mr-2 md:mr-5"
						><a href="/login">로그인</a></button
					>
				</div>
			</div>
		</div>
	</nav>
	<!-- container mx-auto h-screen bg-pink-700 -->
	<div class="h-1/2 mt-7 lg:mt-9 bg-img-top bg-green-100">
		<!-- bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/conference.jpg')] -->
		<!-- bg-gradient-to-r from-gray-300 via-gray-500 to-gray-700 -->
		<!-- <div
			class="w-full h-3 bg-gradient-to-r from-white via-gray-500 to-gray-700 animate-gradient-shift"
		/> -->
		<div class="text-center px-3 lg:px-10 p-20 mt-10">
			<h1
				class="my-4 text-4xl md:text-3xl lg:text-5xl text-pink font-extrabold leading-tight pb-9"
			>
				자기소개서 요약 페이지
			</h1>
			<p class="leading-normal text-black-400 text-base md:text-4xl lg:text-3xl mb-8 ">
				프로메테우스 프로젝트<br>
				변가은, 김지환, 남경현, 이성민, 이대헌, 최민재
			</p>

			<GradientButton size='xl' color="teal"><a href="/summary"> 요약하기 </a></GradientButton>
				
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

<Footer>
  <FooterCopyright href="/" by="Prometheus" year={2023} />
  <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
    <FooterLink href="/">About</FooterLink>
    <FooterLink href="/">Privacy Policy</FooterLink>
    <FooterLink href="/">Licensing</FooterLink>
    <FooterLink href="/">Contact</FooterLink>
  </FooterLinkGroup>
</Footer>


	


<style>
	/* .bg-img-top {
		background: 
			url('/logo1.png');

		/* background-image: url('/bg.jpg'); */
		/* background-repeat: no-repeat;
		background-size: cover; */
	/* } */

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
