import Nav from "./components/Nav"

const Layout = ({children}) => {
  return (
      <body>
          <Nav />
          <main>{ children }</main>
    </body>
  )
}

export default Layout