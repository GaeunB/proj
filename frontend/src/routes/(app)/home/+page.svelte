<script lang="ts">
	import { page } from '$app/stores';
  let banners = [
    "검색",
    "상의",
    "하의",
    "세트",
    "잡화",
    "속옷"
  ];

	

	const buttons = [
			{ text: '검색', color:'pink' },
			{ text: '상의', color:'pink' },
			{ text: '하의', color:'pink'},
			{ text: '세트',  color:'pink'},
			{ text: '잡화',  color:'pink'},
			{ text: '속옷',  color:'pink'},
		];
		
		let activeUrl: string;
	$: {
		activeUrl = $page.url.pathname;
		console.log(`activeUrl:${activeUrl}`);
	}
</script>



<article>
<div class="m-20 w-full max-w-4xl">
	<h1 class="mb-4 text-2xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
		<span class="text-transparent bg-clip-text bg-gradient-to-r to-pink-600 from-pink-400 ">
			쇼핑하기
		</span>
		<p class="mb-10 text-xl text-gray-700 ">
			구매하고자 하는 종류를 선택하세요!
		</p>
		</h1>
		</div>
	</article>

	<div class="grid">
		{#each buttons as button}
			<button class="button {button.color}">
				<a href="/search" >{button.text}</a>
				</button>
		{/each}
	</div>

	<style>
		.grid {
			display: grid;
			grid-template-columns: repeat(3, 1fr);
			gap: 10px;
			margin:20px;
		}
	
		.button {
			display: flex;
			justify-content: center;
			align-items: center;
			width: full; /* 너비 조정 */
			height: 100px; /* 높이 조정 */
			padding: 10px;
			border: none;
			border-radius: 8px;
			font-size: 16px;
			color: white;
			cursor: pointer;
		}

		.button a {
    font-size: 30px; /* 텍스트 크기 조정 */
    margin: 0; /* 내부 여백 제거 */
  }
	
		.pink { background-color: pink; }
		
	</style>
	

	
