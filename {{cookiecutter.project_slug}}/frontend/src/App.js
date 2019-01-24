import React, { Component } from "react";
import { Admin, Resource } from "react-admin";

import logo from "./logo.svg";
import "./App.css";
import { UserList, UserEdit, UserCreate } from "./users";
import LoginPage from "./login";

import dataProvider from "./dataProvider";
import authProvider from "./authProvider";

class App extends Component {
  state = { dataProvider: null };

  componentDidMount() {
    dataProvider().then(dataProvider => this.setState({ dataProvider }));
  }

  render() {
    const { dataProvider } = this.state;

    if (!dataProvider) {
      return (
        <div className="loader-container">
          <div className="loader">Loading...</div>
        </div>
      );
    }
    return (
      <Admin
        title="My React Admin App"
        dataProvider={dataProvider}
        authProvider={authProvider}
        loginPage={LoginPage}
      >
        <Resource
          name="User"
          list={UserList}
          create={UserCreate}
          edit={UserEdit}
        />
        <Resource name="Role" />
      </Admin>
    );
  }
}

export default App;
