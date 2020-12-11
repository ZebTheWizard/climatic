<template>
  <div class="card mt-4 shadow">
    <div class="card-header">
      <div class="card-title m-0">{{ title }}</div>
      <slot name="header"></slot>
    </div>
    <div class="card-body">
      <slot></slot>
      <div class="d-block mt-4" v-if="savable">
        <button
          :class="[
            'btn text-white float-end btn-sm theme-ignore',
            { 'btn-primary': !this.error, 'btn-danger': this.error },
          ]"
          @click="$emit('save')"
        >
          <div
            v-if="saving"
            class="spinner-border spinner-border-sm mx-3"
            role="status"
          ></div>
          <div v-else class="mx-2">
            {{ savable }}
          </div>
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
    saving: {
      type: Boolean,
      default: false,
    },
    error: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style>
</style>