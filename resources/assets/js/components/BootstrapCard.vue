<template>
  <div class="card mt-4">
    <div class="card-header">
      <div class="card-title m-0">{{ title }}</div>
      <slot name="header"></slot>
    </div>
    <div class="card-body">
      <slot></slot>
      <div class="d-block mt-4" v-if="savable">
        <button
          class="btn btn-primary text-white float-end btn-sm"
          @click="$emit('save')"
        >
          {{ savable }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: "Card",
    },
    savable: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>