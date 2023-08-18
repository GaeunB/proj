<script>
	import {
		Card,
		MenuButton,
		Dropdown,
		DropdownItem,
		Avatar,
		Listgroup,
		ListgroupItem
	} from 'flowbite-svelte';
	export let data;
	let properties = ['name', 'phone']; // 사용자 정보 추가
</script>

<div class="m-20">
  <h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl"><span class="text-transparent bg-clip-text bg-gradient-to-r to-pink-600 from-pink-500">나의 정보</span> </h1>
</div>

<div class="flex justify-center items-center">
	<Card padding="sm" class="min-w-[360px]">
		<div class="flex justify-end">
			<MenuButton />
			<Dropdown class="w-36">
				{#if data.accessRole === 'user'}
					<DropdownItem href="/profile/edit" class="text-base font-semibold">수정하기</DropdownItem>
				{/if}
				{#if data.accessRole === 'admin'}
					<DropdownItem href="/profile/edit?userId={data.id}" class="text-base font-semibold"
						>수정하기</DropdownItem
					>
					
				{/if}
			</Dropdown>
		</div>
		<div class="flex flex-col items-center pb-4">
			<Avatar size="lg" />
			<h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">{data.id}</h5>
			
			<div class="mt-8">
				<Listgroup>
					{#each properties as property}
						<ListgroupItem class="text-base font-medium hover:bg-gray-100">
							{data[property]}
						</ListgroupItem>
					{/each}
				</Listgroup>
			</div>
		</div>
	</Card>
</div>
