<template>
  <img alt="Agentic AI" src="./assets/logo.jpg" width="100" height="100">
  <h3>prototype: autogen-issue-resolver</h3>
  <div class="button-container">
    <button @click="start">Start Services</button>
  </div>
  <div class="button-container">
    <button @click="investigate">Investigate</button>
  </div>
  <div class="logs-container">
    <div class="logs" v-if="logs1">
      <h4>Logs Svc1:</h4>
      <pre class="console">{{ logs1 }}</pre>
    </div>
    <div class="logs" v-if="logs2">
      <h4>Logs Svc2:</h4>
      <pre class="console">{{ logs2 }}</pre>
    </div>
    <div class="logs" v-if="logs3">
      <h4>Logs Svc3:</h4>
      <pre class="console">{{ logs3 }}</pre>
    </div>
  </div>
  <h4>Agent Logs:</h4>
  <div v-if="conclusion">{{ conclusion.conclusion }}</div>
  <div v-if="agentlogs">
    <pre class="console">{{ agentlogs }}</pre>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      logs1: null,
      logs2: null,
      logs3: null,
      agentlogs: null,
      conclusion: null
    };
  },
  mounted() {
    this.fetchLogs1();
    this.fetchLogs2();
    this.fetchLogs3();
    this.fetchAgentlogs();
    this.fetchConclusion();
  },
  created() {
    setInterval(() => {
      this.fetchLogs1();
      this.fetchLogs2();
      this.fetchLogs3();
    }, 500);
  },
  methods: {
    async fetchLogs1() {
      try {
        var response = await axios.get('/viewlogs1');
        this.logs1 = response.data;
      } catch (error) {
        console.error('Error fetching logs from service 1:', error);
      }
    },
    async fetchLogs2() {
      try {
        var response = await axios.get('/viewlogs2');
        this.logs2 = response.data;
      } catch (error) {
        console.error('Error fetching logs from service 2:', error);
      }
    },
    async fetchLogs3() {
      try {
        var response = await axios.get('/viewlogs3');
        this.logs3 = response.data;
      } catch (error) {
        console.error('Error fetching logs from service 3:', error);
      }
    },
    async fetchAgentlogs() {
      try {
        var response = await axios.get('/agentlogs');
        this.agentlogs = response.data;
      } catch (error) {
        console.error('Error fetching logs from Agents:', error);
      }
    },
    async fetchConclusion() {
      try {
        var response = await axios.get('/conclusion');
        this.conclusion = response.data;
      } catch (error) {
        console.error('Error fetching conclusion from Agents:', error);
      }
    },
    async start() {
      axios.get('/start');
    },
    async investigate() {
      await axios.get('/investigate');
      await this.fetchAgentlogs();
      await this.fetchConclusion();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}
.console {
  font-family: 'Courier New', Courier, monospace;
  font-size: x-small;
  text-align: left;
  color: white;
  background-color: black;
  padding: 10px;
}
.logs-container {
  display: flex;
  justify-content: space-around;
}
.logs {
  width: 30%;
}
img {
  border: #2c3e50 5px solid;
}
.button-container {
  margin: 10px;
}
</style>