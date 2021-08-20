<template>
  <div>
    <div v-for="account of accounts" class="card mb-4">
        <div class="card-header">
          <h6 class="font-weight-bold text-primary">{{ account.title }}</h6>
        </div>
        <div class="table-responsive">
          <table class="table table-sm">
            <thead>
              <tr role="row">
                <th>Account</th>
                <th>Balance</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="child of account.children">
                <td>{{ child.title }}</td>
                <td class="font-weight-bold">{{ child.account_balance }}</td>
              </tr>
            </tbody>
          </table>      
        </div>
        <div class="card-header">
            {{ account.title }} total: <span class="font-weight-bold">{{ account.account_balance }}</span>
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
  data () {
    return {
      accounts: this.getAccountsBalance(),
      total: 0,
    }
  },

  methods: {
    getAccountsBalance() {
      axios
        .get('/accounts-balance/')
        .then((response) => {

          this.accounts = response.data;

          // Calculate total available funds
          for (var account of this.accounts) {
            this.total += account.account_balance;
          }

          // Make nested structure
          this.accounts = this.$nestObjects(this.accounts);

          // Calculate subtotal for an parent account
          for (var account of this.accounts) {
            var accountBalance = 0;
            for (var child of account.children) {
              accountBalance += child.account_balance;
            }
            account.account_balance = accountBalance;
          }
        })
    },
  },
  computed: {

  },
}
</script>

<style>
</style>
