<script lang="ts">
	import { page } from '$app/stores';
	import { Textarea, Toolbar, ToolbarGroup, ToolbarButton, Button, GradientButton, Heading } from 'flowbite-svelte';
 
		let activeUrl: string;
	$: {
		activeUrl = $page.url.pathname;
		console.log(`activeUrl:${activeUrl}`);
	}
</script>



<article>
<div class="m-20 w-full max-w-4xl">
	<h1 class="mb-4 text-2xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
		<Heading tag="h1" >요약하기</Heading>
		<p class="mb-10 text-xl text-gray-700 ">
			요약하고자하는 자기소개서를 입력해주세요!
		</p>
		</h1>
		</div>
	</article>

	<form>
		<Textarea class="mb-4" placeholder="Write a comment">
			<div slot="footer" class="flex items-center justify-between">
				<GradientButton type="submit" outline color="greenToBlue">요약하기</GradientButton>
				<Toolbar embedded>
					<ToolbarButton name="Attach file"></ToolbarButton>
					<ToolbarButton name="Set location"></ToolbarButton>
					<ToolbarButton name="Upload image"></ToolbarButton>
				</Toolbar>
			</div>
		</Textarea>
	</form>



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
	

	
