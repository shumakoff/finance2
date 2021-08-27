<template>
  <div>
    <div class="card">

      <div class="card-header">
        <h6 class="font-weight-bold text-primary">Recent entries</h6>
      </div>

      <div class="card-body">

        <div class="table-responsive">
          <table class="table table-sm">

            <thead>
              <tr role="row">
                <th>Data</th>
                <th>Entry</th>
                <th>Value</th>
                <th>Currency</th>
              </tr>
            </thead>

            <tbody>
              <tr v-on:click="$emit('showentryform', record.id)" v-for="record of recentRecords.results">
                <td>{{ record.date }}</td>
                <td>{{ record.item }}</td>
                <td v-if="accounts[record.account]['acc']['currency'] == 'BTC'">{{ record.value }}</td>
                <td v-else>{{ record.value|numeral('0,0.[00]') }}</td>
                <td>{{ accounts[record.account]['acc']['currency'] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

        <div class="card-footer">
          <div class="col text-center">
            <a v-on:click="loadRecentRecords(recentRecords.previous)" class="btn btn-primary btn-sm">
              <span class="icon text-white-50">
                  <font-awesome-icon icon="arrow-left" />
              </span>
              <span class="text"></span>
            </a>
            <a v-on:click="loadRecentRecords(recentRecords.next)" class="btn btn-primary btn-sm">
              <span class="icon text-white-50">
                  <font-awesome-icon icon="arrow-right" />
              </span>
              <span class="text"></span>
            </a>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  components: {
  },
  props: [],
  data () {
    return {
      recentRecords: 0,
      category: 0,
      accounts: 0,
      record: 0,
      account: 0,
    }
  },

  mounted() {
    this.loadAccounts();
  },
  
  created () {
  },

  methods: {
    loadRecentRecords(page) {
      var url = '/records/';
      if (page != undefined) {
        var page_num = page.split('=')[1];
        if (page_num != undefined) {
          url += '?page=' + page_num;
      }}
      axios
        .get(url)
        .then((response) => { 
          this.recentRecords = response.data;
        });
    },

    loadAccounts() {
      axios
        .get('/accounts/')
        .then((response) => { 
          this.accounts = response.data;
          var result = {};
          for (var acc of this.accounts) {
            result[acc.id] = {acc};
          }
          this.accounts = result;
          this.loadRecentRecords()
          }
        )
    },
    
  },
  computed: {

  },
}
</script>

<style>
</style>
