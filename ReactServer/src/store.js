import { configureStore, createSlice } from "@reduxjs/toolkit";

let records = createSlice({
  name: "records",
  initialState: [
    { 챔피언: "가렌", 승패: "승", KDA: "21:0:1" },
    { 챔피언: "카타리나", 승패: "승", KDA: "4:21:4" },
  ],
});

let users = createSlice({
  name: "users",
  initialState: [
    { 넘버: "1", 이름: "문성준", 승패: "승", KDA: "20/0/8" },
    { 넘버: "2", 이름: "엄준식", 승패: "패", KDA: "0/20/1" },
  ],
});

export default configureStore({
  reducer: {
    records: records.reducer,
    users: users.reducer,
  },
});
