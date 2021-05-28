<template>
  <v-container v-if="$auth.loggedIn" fluid>
    <v-card>
      <v-card-title>
        <h2>Create token</h2>
      </v-card-title>
      <v-divider />
      <v-card-text>
        <v-form v-model="valid" @submit.prevent="submit">
          <v-container>
            <v-row>
              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  v-model="item.tokenId"
                  :rules="tokenIdRules"
                  :counter="42"
                  label="Token ID"
                  required
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  v-model="item.address"
                  :rules="addressRules"
                  :counter="42"
                  label="Ethereum adress"
                  required
                />
              </v-col>
            </v-row>
            <v-row style="padding: 10px">
              <v-btn
                class="mr-4"
                type="submit"
                :disabled="!valid"
              >
                submit
              </v-btn>
              <v-btn @click="clear">
                clear
              </v-btn>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
    </v-card>
    <v-card style="margin-top: 50px">
      <v-card-title>
        <h2>List of tokens</h2>
      </v-card-title>
      <v-divider />
      <v-data-table
        v-model="selectedToken"
        :headers="headers"
        :items="tokens"
        :items-per-page="5"
        :single-select="true"
        item-key="pk"
        show-select
        dense
      />
    </v-card>
    <v-card v-if="selectedToken[0]" style="margin-top: 50px">
      <v-card-title>
        <h2>Transfer token to</h2>
      </v-card-title>
      <v-divider />
      <v-card-text>
        <v-form v-model="valid2" @submit.prevent="transfer">
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="transferTo"
                  :rules="addressRules"
                  :counter="42"
                  label="Ethereum adress"
                  required
                />
              </v-col>
            </v-row>
            <v-row style="padding: 10px">
              <v-btn
                class="mr-4"
                type="submit"
                :disabled="!valid2"
              >
                submit
              </v-btn>
              <v-btn @click="clear">
                clear
              </v-btn>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
    </v-card>
    <v-card v-if="selectedToken[0] ? !tokens.find(o => o.pk === selectedToken[0].pk).metadata : false" :disabled="selectedToken.length < 1" style="margin-top: 50px">
      <v-card-title>
        <h2>Add metadata to the Token</h2>
      </v-card-title>
      <v-divider />
      <v-card-text>
        <v-form @submit.prevent="submitMeta">
          <v-container>
            <v-row>
              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  v-model="metadata.title"
                  :counter="20"
                  label="Title"
                  required
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  v-model="metadata.type"
                  :counter="20"
                  label="Type"
                  required
                />
              </v-col>

              <v-col
                cols="12"
                md="4"
              >
                <v-text-field
                  v-model="metadata.name"
                  :counter="20"
                  label="Name"
                  required
                />
              </v-col>
            </v-row>
            <v-row>
              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  v-model="metadata.description"
                  :counter="120"
                  label="Description"
                  required
                />
              </v-col>

              <v-col
                cols="12"
                md="6"
              >
                <v-text-field
                  v-model="metadata.content"
                  :counter="120"
                  label="Content"
                  required
                />
              </v-col>
            </v-row>
            <v-row style="padding: 10px">
              <v-btn
                class="mr-4"
                type="submit"
              >
                submit
              </v-btn>
              <v-btn @click="clearMeta">
                clear
              </v-btn>
            </v-row>
          </v-container>
        </v-form>
      </v-card-text>
    </v-card>
    <v-card v-if="selectedToken[0] ? tokens.find(o => o.pk === selectedToken[0].pk).metadata : false" :disabled="selectedToken.length < 1" style="margin-top: 50px">
      <v-card-title>
        <h2>Token`s metadata</h2>
      </v-card-title>
      <v-divider />
      <v-card-text>
        <v-chip style="margin-top: 10px" color="orange" large>
          <h3>Title</h3>
        </v-chip> _ <v-chip style="margin-top: 10px" color="green" large>
          {{ tokens.find(o => o.pk === selectedToken[0].pk).metadata.title }}
        </v-chip> <br>
        <v-chip style="margin-top: 10px" color="orange" large>
          <h3>Type</h3>
        </v-chip> _ <v-chip style="margin-top: 10px" color="green" large>
          {{ tokens.find(o => o.pk === selectedToken[0].pk).metadata.type }}
        </v-chip> <br>
        <v-chip style="margin-top: 10px" color="orange" large>
          <h3>Name</h3>
        </v-chip> _ <v-chip style="margin-top: 10px" color="green" large>
          {{ tokens.find(o => o.pk === selectedToken[0].pk).metadata.name }}
        </v-chip> <br>
        <v-chip style="margin-top: 10px" color="orange" large>
          <h3>Description</h3>
        </v-chip> _ <v-chip style="margin-top: 10px" color="green" large>
          {{ tokens.find(o => o.pk === selectedToken[0].pk).metadata.description }}
        </v-chip> <br>
        <v-chip style="margin-top: 10px" color="orange" large>
          <h3>Content</h3>
        </v-chip> _ <v-chip style="margin-top: 10px" color="green" large>
          {{ tokens.find(o => o.pk === selectedToken[0].pk).metadata.content }}
        </v-chip>
      </v-card-text>
    </v-card>
  </v-container>
  <div v-else style="margin-top:50px">
    <v-card>
      <v-card-text>
        <h1>Login first!</h1>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    valid2: false,
    item: {
      pk: '',
      user: '',
      tokenId: '',
      address: ''
    },
    metadata: {
      token: '',
      title: '',
      type: '',
      name: '',
      description: '',
      content: ''
    },
    transferTo: '',
    selectedToken: [],
    tokens: [],
    tokenIdRules: [
      v => !!v || 'Token ID is required',
      v => v.length <= 42 || 'Token ID be less than 42 characters'
    ],
    addressRules: [
      v => !!v || 'Ethereum address is required',
      v => /^0x[a-fA-F0-9]{40}$/.test(v) || 'Ethereum address must be valid'
    ],
    headers: [
      { text: 'Token ID', value: 'tokenId' },
      { text: 'Address', value: 'address' }
    ]
  }),
  mounted () {
    this.fetchTokens()
  },
  methods: {
    async submit () {
      this.item.user = this.$auth.$state.user.id
      const response = await this.$axios.$post(
        '/api/basetoken/',
        this.item
      )
      this.clear()
      this.fetchTokens()
      console.log(response)
    },
    async fetchTokens () {
      this.item.user = this.$auth.$state.user.id
      const response = await this.$axios.$get(
        '/api/basetoken/'
      )
      this.tokens = response
      console.log(this.tokens)
    },
    clear () {
      this.item.tokenId = ''
      this.item.address = ''
    },
    clearMeta () {
      this.metadata.title = ''
      this.metadata.type = ''
      this.metadata.name = ''
      this.metadata.description = ''
      this.metadata.content = ''
    },
    async submitMeta () {
      this.metadata.token = this.selectedToken[0].pk
      const response = await this.$axios.$post(
        '/api/metadata/',
        this.metadata
      )
      this.clearMeta()
      console.log(response)
    },
    transfer () {
      const tokn = this.tokens.find(o => o.pk === this.selectedToken[0].pk)
      tokn.address = this.transferTo
      const response = this.$axios.$put(`/api/basetoken/${tokn.pk}/`, tokn)
      this.transferTo = ''
      console.log(response)
    }
  }
}
</script>
