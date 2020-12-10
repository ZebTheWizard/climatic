<template>
  <div>
    <button class="btn btn-link" @click="manual = !manual">
      Toggle manual entry
    </button>
    <div v-if="manual">
      <bootstrap-card savable="Save" title="Input Single Entry">
        Create something cool
      </bootstrap-card>

      <bootstrap-card savable="Upload" title="Entries from CSV">
        Create something cool
      </bootstrap-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      manual: false,
    };
  },
};
</script>

