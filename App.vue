<template>
  <RouterView />
  <Toaster position="top-right" :rich-colors="true" />
</template>

<script setup lang="ts">
import { Toaster } from 'vue-sonner'
</script>
