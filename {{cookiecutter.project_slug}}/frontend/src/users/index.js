import React from "react";
import {
  BooleanField,
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  ReferenceArrayInput,
  required,
  SelectArrayInput,
  SimpleForm,
  TextField,
  TextInput
} from "react-admin";

export const UserList = props => (
  <List {...props}>
    <Datagrid>
      <TextField source="firstName" />
      <TextField source="lastName" />
      <TextField source="email" />
      <BooleanField source="active" />
      <EditButton />
    </Datagrid>
  </List>
);

const EditCreateForm = props => (
  <SimpleForm>
    <TextInput source="firstName" />
    <TextInput source="lastName" />
    <TextInput source="email" />
    <TextInput source="password" />
    <ReferenceArrayInput label="Roles" source="roleIds" reference="Role">
      <SelectArrayInput optionText="name" />
    </ReferenceArrayInput>
  </SimpleForm>
);

export const UserEdit = props => (
  <Edit {...props}>
    <EditCreateForm />
  </Edit>
);

export const UserCreate = props => (
  <Create {...props}>
    <EditCreateForm />
  </Create>
);
