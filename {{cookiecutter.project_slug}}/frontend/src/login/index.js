import React, { Component } from "react";
import { connect } from "react-redux";
import { compose } from "redux";
import { reduxForm, Field } from "redux-form";
import { userLogin, Notification } from "react-admin";
import {
  MuiThemeProvider,
  createMuiTheme,
  withStyles
} from "@material-ui/core/styles";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CircularProgress from "@material-ui/core/CircularProgress";
import TextField from "@material-ui/core/TextField";
import LockIcon from "@material-ui/icons/Lock";

const lightTheme = {
  palette: {
    secondary: {
      light: "#5f5fc4",
      main: "#283593",
      dark: "#001064",
      contrastText: "#fff"
    }
  }
};

const styles = theme => ({
  main: {
    display: "flex",
    flexDirection: "column",
    minHeight: "100vh",
    alignItems: "center",
    justifyContent: "flex-start",
    background: "url(https://source.unsplash.com/random/1600x900)",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover"
  },
  card: {
    minWidth: 300,
    marginTop: "6em"
  },
  avatar: {
    margin: "1em",
    display: "flex",
    justifyContent: "center"
  },
  icon: {
    backgroundColor: theme.palette.secondary.main
  },
  form: {
    padding: "0 1em 1em 1em"
  },
  input: {
    marginTop: "1em"
  },
  actions: {
    padding: "0 1em 1em 1em"
  }
});

const renderInput = ({
  meta: { touched, error } = {},
  input: { ...inputProps },
  ...props
}) => (
  <TextField
    error={!!(touched && error)}
    helperText={touched && error}
    {...inputProps}
    {...props}
    fullWidth
  />
);

class LoginPage extends Component {
  submit = e => {
    e.preventDefault();

    const credentials = {
      email: e.target[0].value,
      password: e.target[1].value
    };

    this.props.userLogin(credentials);
  };

  render() {
    const { classes, isLoading } = this.props;

    return (
      <MuiThemeProvider theme={createMuiTheme(lightTheme)}>
        <div className={classes.main}>
          <Card className={classes.card}>
            <div className={classes.avatar}>
              <Avatar className={classes.icon}>
                <LockIcon />
              </Avatar>
            </div>

            <form onSubmit={this.submit}>
              <div className={classes.form}>
                <div className={classes.input}>
                  <Field
                    autoFocus
                    name="email"
                    component={renderInput}
                    label={"Email"}
                    disabled={isLoading}
                  />
                </div>

                <div className={classes.input}>
                  <Field
                    name="password"
                    component={renderInput}
                    label={"Password"}
                    type="password"
                    disabled={isLoading}
                  />
                </div>
              </div>

              <CardActions className={classes.actions}>
                <Button
                  variant="raised"
                  type="submit"
                  color="primary"
                  disabled={isLoading}
                  className={classes.button}
                  fullWidth
                >
                  {isLoading && <CircularProgress size={25} thickness={2} />}
                  Sign In
                </Button>
              </CardActions>
            </form>
          </Card>

          <Notification />
        </div>
      </MuiThemeProvider>
    );
  }
}

const mapStateToProps = state => ({ isLoading: state.admin.loading > 0 });

export default compose(
  reduxForm({
    form: "signIn",
    validate: values => {
      const errors = {};
      if (!values.email) {
        errors.email = "Required";
      }
      if (!values.password) {
        errors.password = "Required";
      }
      return errors;
    }
  }),
  connect(
    mapStateToProps,
    { userLogin }
  ),
  withStyles(styles)
)(LoginPage);
