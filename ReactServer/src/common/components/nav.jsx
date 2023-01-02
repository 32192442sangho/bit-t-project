import { Navbar, Container, Nav } from "react-bootstrap";

const Navb = () => {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">Myteach</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/records">record</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
};

export default Navb;
