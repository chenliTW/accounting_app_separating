<template>
  <div class="container">
    <h1>記帳應用</h1>

    <!-- 新增記錄的表單 -->
    <form @submit.prevent="createAccount" class="account-form">
      <div>
        <label for="description">說明:</label>
        <input id="description" v-model="newAccount.description" type="text" placeholder="請輸入記帳說明" required />
      </div>
      <div>
        <label for="amount">金額:</label>
        <input id="amount" v-model.number="newAccount.amount" type="number" placeholder="請輸入金額" required />
      </div>
      <button type="submit">新增記錄</button>
    </form>

    <!-- 顯示記錄列表 -->
    <h2>記錄列表</h2>
    <table class="account-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>說明</th>
          <th>金額</th>
          <th>時間</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="account in accounts" :key="account.id">
          <td>{{ account.id }}</td>
          <td>{{ account.description }}</td>
          <td>{{ account.amount }}</td>
          <td>{{ formatDate(account.timestamp) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 記錄列表與表單資料
const accounts = ref([])
const newAccount = ref({
  description: '',
  amount: 0,
})

// 讀取記錄
const fetchAccounts = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/accounts')
    if (response.ok) {
      accounts.value = await response.json()
    } else {
      console.error('讀取記錄失敗:', response.statusText)
    }
  } catch (error) {
    console.error('讀取記錄發生錯誤:', error)
  }
}

// 新增記錄
const createAccount = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/accounts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newAccount.value),
    })
    if (response.ok) {
      const created = await response.json()
      // 新增成功後加入列表，並清空表單
      accounts.value.push(created)
      newAccount.value.description = ''
      newAccount.value.amount = 0
    } else {
      console.error('新增記錄失敗:', response.statusText)
    }
  } catch (error) {
    console.error('新增記錄發生錯誤:', error)
  }
}

// 格式化日期字串
const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleString()
}

// 組件掛載時讀取記錄
onMounted(() => {
  fetchAccounts()
})
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: Arial, sans-serif;
}

h1,
h2 {
  text-align: center;
}

.account-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.account-form label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.account-form input {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
}

.account-form button {
  align-self: flex-start;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: #42b983;
  border: none;
  color: #fff;
  cursor: pointer;
}

.account-form button:hover {
  background-color: #36966e;
}

.account-table {
  width: 100%;
  border-collapse: collapse;
}

.account-table th,
.account-table td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: left;
}

.account-table th {
  background-color: #f4f4f4;
}
</style>
