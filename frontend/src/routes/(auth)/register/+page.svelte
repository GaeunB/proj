<script>
	import { Input, Label, Checkbox, Button, A, Card } from 'flowbite-svelte';
	export let form;
</script>

<Card class="max-w-lg mx-auto mt-8 mb-8">
	<div>
		<form action="?/register" method="POST">
			<div class="grid gap-6 mb-6 md:grid-cols-2">
				<!-- <div>
					<Label for="id" class="mb-2 text-pink-400">ID</Label>
					<Input type="text" id="id" name="id" placeholder="kangin" required />
				</div> -->
				<div>
					<Label for="name" class="mb-2 text-pink-400">이름</Label>
					<Input type="text" id="name" name="pink" placeholder="이강인" required />
				</div>
				<div>
					<Label for="phone" class="mb-2 text-pink-400">📞전화번호</Label>
					<Input type="tel" id="phone" name="phone" placeholder="010-0000-1111" required />
				</div>
				<!-- <div class="grid grid-cols-2 gap-6">
				<Radio
					name="role"
					class="w-full p-4 bg-white"
					bind:group={colors}
					color="purple"
					value="admin">admin</Radio
				>
				<Radio
					name="role"
					class="w-full p-4 bg-white"
					bind:group={colors}
					color="purple"
					value="user">user</Radio
				>
			</div> -->
			</div>
			<!-- <div class="mb-6">
				<Label for="email" class="mb-2 text-indigo-400">✉️ Email address</Label>
				<Input type="email" id="email" name="email" placeholder="kangin@gmail.com" required />
			</div> -->
			{#if form?.incorrecting}<p class="error text-red-500">비밀번호가 다릅니다.</p>{/if}
			<!--incorrect (x) incorrecting (o)-->
			<div class="mb-6">
				<Label for="password" class="mb-2 text-pink-400">🔒 비밀번호</Label>
				<Input type="password" id="password" name="password" placeholder="•••••••••" required />
			</div>
			<div class="mb-6">
				<Label for="confirm_password" class="mb-2 text-pink-400">✔️ 비밀번호 확인</Label>
				<Input
					type="password"
					id="confirm_password"
					name="confirm_password"
					placeholder="•••••••••"
					required
				/>
			</div>
			<Checkbox checked color="red" class="mb-6 space-x-1 text-pink-400" required
				>약관에 동의합니다. <A href="/" class="text-pink-400 hover:underline"
					>이용약관</A
				>.</Checkbox
			>
			<Button
				type="submit"
				class="bg-pink-500 font-semibold hover:text-pink-500 hover:bg-pink-400">가입하기</Button
			>
		</form>
	</div>
</Card>
