<script lang="ts">
	export let data;
	import { page } from '$app/stores';
	import { Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
  import { Icon } from 'flowbite-svelte-icons';

	let activeUrl: string;
	$: {
		activeUrl = $page.url.pathname;
		console.log(`activeUrl:${activeUrl}`);
	}
	let activeClass = 'flex items-center p-2 text-base font-normal text-primary-900 bg-primary-200 dark:bg-primary-700 rounded-lg dark:text-white hover:bg-primary-100 dark:hover:bg-gray-700';
  let nonActiveClass = 'flex items-center p-2 text-base font-normal text-green-900 rounded-lg dark:text-white hover:bg-green-100 dark:hover:bg-green-700';
</script>


<Navbar let:hidden let:toggle rounded color="pink">
  <NavBrand href="/">
    <img src="logo1.png" class="mr-3 h-6 sm:h-9" alt="청바지몰 로고" />
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-pink-500">청바지몰</span>
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi href="/" active={true}>홈</NavLi>
    <NavLi href="#">검색하기</NavLi>
    <NavLi href="#">장바구니</NavLi>
    <NavLi href="#">나의 정보</NavLi>
    <NavLi href="#">고객센터</NavLi>
  </NavUl>
</Navbar>



<section class="flex flex-1">
	<div>
		<Sidebar color="gray">
			<SidebarWrapper>
				<SidebarGroup>
					<SidebarItem label="홈" href="/home" active={activeUrl === '/home'}>
						
						<svelte:fragment slot="icon">
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
									d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z"
								/></svg
							>
						</svelte:fragment>
					</SidebarItem>
					<SidebarItem label="검색" href="/search" active={activeUrl === '/search'}>
						<svelte:fragment slot="icon">
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
									d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
								/></svg
							>
						</svelte:fragment>
					</SidebarItem>
					<SidebarItem label="장바구니" href="/statistics" active={activeUrl === '/statistics'}>
						<svelte:fragment slot="icon">
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
									d="M1 1v14h16m0-9-3-2-3 5-3-2-3 4"
								/></svg
							>
						</svelte:fragment>
					</SidebarItem>
					<SidebarItem label="나의 정보" href="/profile" active={activeUrl === '/profile'}>
						<svelte:fragment slot="icon">
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
									d="M3.656 12.115a3 3 0 0 1 5.682-.015M13 5h3m-3 3h3m-3 3h3M2 1h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Zm6.5 4.5a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z"
								/></svg
							>
						</svelte:fragment>
					</SidebarItem>
					
					
					{#if data.role === 'admin'}
						<SidebarItem label="고객센터" href="/userlist" active={activeUrl === '/userlist'}>
							<svelte:fragment slot="icon">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 24 24"
									stroke-width="1.5"
									stroke="currentColor"
									class="w-6 h-6"
									><path
										d="M14 3a3 3 0 1 1-1.614 5.53M15 12a4 4 0 0 1 4 4v1h-3.348M10 4.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0ZM5 11h3a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"
									/></svg
								>
							</svelte:fragment>
						</SidebarItem>
						{/if}
						<SidebarItem label="로그아웃" href="/logout" active={activeUrl === '/'}>
							<svelte:fragment slot="icon">
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
										d="M4 8h11m0 0-4-4m4 4-4 4m-5 3H3a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h3"
									/></svg
								>
							</svelte:fragment>
						</SidebarItem>
				</SidebarGroup>
			</SidebarWrapper>
		</Sidebar>
	</div>
	<div class="flex-1 justify-center">
		<slot />
	</div>
</section>
