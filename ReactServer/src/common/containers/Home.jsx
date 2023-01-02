// 외부 라이브러리
import { Route, Routes, useParams } from "react-router-dom";

// 내부 모듈
import { Access } from "../../main";
import { Navb, Footer } from "..";
import { Records } from "../../playlist";

const Home = () => {
  let { id } = useParams();
  return (
    <>
      <Navb />
      <Routes>
        <Route path="/" element={<Access />}></Route>
        <Route path="/records/:id" element={<Records />}></Route>
        <Route path="/*" element={<h1>없는 페이지에유</h1>}></Route>
      </Routes>
      <Footer />
    </>
  );
};

export default Home;
