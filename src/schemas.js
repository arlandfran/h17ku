import { object, string } from "yup";

export const registerSchema = object({
  email: string().required().email(),
  username: string().min(4).matches(/^\S*$/, "no spaces allowed").required(),
  password: string().min(8).matches(/^\S*$/, "no spaces allowed").required(),
  password2: string()
    .min(8, "password must be at least 8 characters")
    .matches(/^\S*$/, "no spaces allowed")
    .required("confirm password is a required field"),
});

export const loginSchema = object({
  email: string().email().required(),
  password: string().required(),
});
