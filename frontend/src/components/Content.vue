<template>

  <!-- body -->
  <div id="wrapper">
    <!-- sidebar -->
    <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" v-bind:class="{ toggled: sidebarToggled }" id="accordionSidebar">
      <!-- Sidebar - Brand -->
      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="/">
          <div class="sidebar-brand-icon">
              <i class="fas fa-landmark"></i>
          </div>
          <div class="sidebar-brand-text mx-3">F2</div>
      </a>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">

      <!-- Nav Item - Dashboard -->
      <router-link
        to="/" exact
        v-slot="{ href, route, navigate, isActive, isExactActive }"
        custom>
        <li class="nav-item" :class="[isActive && 'active']">
          <a class="nav-link" :href="href" @click="navigate">
            <font-awesome-icon icon="chart-area"/>
            <span>{{ route.name }}</span>
          </a>
        </li>
      </router-link>

      <!-- Nav Item - Records -->
      <router-link
        to="records"
        v-slot="{ href, route, navigate, isActive, isExactActive }"
        custom>
        <li class="nav-item" :class="[isActive && 'active']">
          <a class="nav-link" :href="href" @click="navigate"><span>{{ route.name }}</span></a>
        </li>
      </router-link>

      <!-- Nav Item - Stats -->
      <router-link
        to="stats"
        v-slot="{ href, route, navigate, isActive, isExactActive }"
        custom>
        <li class="nav-item" :class="[isActive && 'active']">
          <a class="nav-link" :href="href" @click="navigate"><span>{{ route.name }}</span></a>
        </li>
      </router-link>

      <div class="text-center d-none d-md-inline">
          <font-awesome-icon v-on:click="toggleSidebar" :icon="collapsedIcon" />
      </div>

    </ul>
    <!-- end of sidebar -->

    <div id="content-wrapper" class="d-flex flex-column">
      <div id="content">
        <notifications group="alertSuccess" classes="alert alert-primary alert-dismissible fade show"/>
        <notifications group="alertFail" classes="alert alert-danger alert-dismissible fade show"/>
        <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">
          <button v-on:click="toggleSidebar" id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
            <font-awesome-icon icon="bars" />
          </button>
          <search-form/>
          <new-entry-button v-on:showentryform="showNewEntryForm"/>
        </nav>
        <template v-if="newEntryFormVisible">
          <template v-if="recordId != 0">
            <new-entry-form v-on:showentryform="showNewEntryForm" v-bind:recordId="recordId"></new-entry-form>
          </template>
          <template v-else>
            <new-entry-form v-on:showentryform="showNewEntryForm"></new-entry-form>
          </template>
        </template>
        <router-view v-on:showentryform="showNewEntryForm($event)"/>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import Dashboard from '../components/Dashboard.vue'
import Stats from '../components/Stats.vue'
import SearchForm from '../components/SearchForm.vue'
import NewEntryButton from '../components/NewEntryButton.vue'
import NewEntryForm from '../components/NewEntryForm.vue'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'

export default {
  components: {
    'Dashboard': Dashboard,
    'search-form': SearchForm,
    'new-entry-button': NewEntryButton,
    'new-entry-form': NewEntryForm,
  },
  data () {
    return {
      newEntryFormVisible: false,
      sidebarToggled: false,
      recordId: 0,
    }
  },

  methods: {
    log(message) {
      console.log(message);
    },

    toggleSidebar() {
      this.sidebarToggled = !this.sidebarToggled;
    },

    showNewEntryForm(recordId) {
      this.newEntryFormVisible = !this.newEntryFormVisible;
      this.recordId = recordId;
    },

  },
  computed: {

    collapsedIcon() {
      if (!this.sidebarToggled) {
        return faArrowLeft;
      } else {
        return faArrowRight;
      }
    },


  },
}
</script>

<style>
</style>
