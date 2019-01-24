import {
  AUTH_LOGIN,
  AUTH_LOGOUT,
  AUTH_ERROR,
  AUTH_CHECK,
  AUTH_GET_PERMISSIONS
} from "react-admin";
import { login, logout } from "./graphql";

export default async (type, params) => {
  if (type === AUTH_LOGIN) {
    const { email, password } = params;
    if (!email || !password) {
      return Promise.reject();
    }
    return login(email, password);
  }
  // called when the user clicks on the logout button
  if (type === AUTH_LOGOUT) {
    localStorage.removeItem("email");
    localStorage.removeItem("token");
    return logout();
  }
  // called when the API returns an error
  if (type === AUTH_ERROR) {
    const { status } = params;
    if (status === 401 || status === 403) {
      localStorage.removeItem("email");
      localStorage.removeItem("token");
      return Promise.reject();
    }
    return Promise.resolve();
  }
  // called when the user navigates to a new location
  if (type === AUTH_CHECK) {
    return localStorage.getItem("token") ? Promise.resolve() : Promise.reject();
  }

  if (type === AUTH_GET_PERMISSIONS) {
    const roles = localStorage.getItem("roles").split(",");
    return roles ? Promise.resolve(roles) : Promise.reject();
  }
  return Promise.reject("Unknown method");
};
