<script>
	import { Label, Input, Card } from 'flowbite-svelte';
	let show = false;
	export let form;
	import { enhance } from '$app/forms';
</script>

<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
	<div class="sm:mx-auto sm:w-full sm:max-w-sm">
		<img class="mx-auto h-0 w-auto" src="/logo1.png" alt="Your Company" />
		<h2 class="mt-5 text-center text-2xl font-bold leading-9 tracking-tight text-pink-500">
			로그인하기
		</h2>
	</div>
	<Card class="px-6 mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
		<form use:enhance class="space-y-5" action="?/login" method="POST">
			<div>
				<Label for="id" class="mb-2.5 text-pink-400">전화번호</Label>
				<Input id="id" name="id" type="text" placeholder="전화번호를 입력하세요." size="md" />
			</div>
			<div>
				<Label for="password" class="mb-2.5 text-pink-400">비밀번호</Label>
				<Input
					id="password"
					name="password"
					type={show ? 'text' : 'password'}
					placeholder="비밀번호를 입력하세요."
					size="lg"
				>
					<button slot="left" on:click={() => (show = !show)} class="pointer-events-auto">
						{#if show}
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
								><path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z"
								/><path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								/></svg
							>
						{:else}
							<svg
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
								stroke-width="1.5"
								stroke="currentColor"
								class="w-6 h-6"
								><path
									stroke-linecap="round"
									stroke-linejoin="round"
									d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88"
								/></svg
							>
						{/if}
					</button>
				</Input>
			</div>
			<div class="mt-7">
				<button
					type="submit"
					class="flex w-full justify-center rounded-md bg-pink-400 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:text-pink-500 hover:bg-pink-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-pink-500"
					>로그인</button
				>
			</div>
			{#if form?.incorrect}<p class="error text-red-500">{form.message}</p>{/if}
		</form>

		<!-- <div class="mt-5 text-center text-sm">
			<a href="#" class="font-semibold text-indigo-500 hover:text-pink-400">비밀번호를 잊어버리셨나요?</a>
		</div> -->
		<p class="mt-5 text-center text-sm text-gray-500">
			
			<a href="/register" class="flex w-full justify-center rounded-md bg-pink-400 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:text-pink-500 hover:bg-pink-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-pink-500"
				>회원가입하기</a
			>
		</p>
	</Card>
</div>
