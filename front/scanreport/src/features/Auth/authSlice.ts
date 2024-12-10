import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { CurrentUser } from 'features/User/UserType';

export interface AuthState {
    logged: boolean;
    user: CurrentUser | null;
  }

const initialState: AuthState = {
  logged: false,
  user: null
}


const auth = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    resetAuthState: state => {
        Object.assign(state, initialState);
    },
    authLogin: (state, action: PayloadAction<CurrentUser>) => {
        state.logged = true
        state.user = action.payload
    },
    updateAuthUser: (state, action: PayloadAction<CurrentUser>) => {
      state.logged = true
      state.user!.id = action.payload.id
      state.user!.email = action.payload.email
      state.user!.firstname = action.payload.firstname
      state.user!.lastname = action.payload.lastname
      state.user!.token = action.payload.token
    },
    
  },
  extraReducers: (builder) => {},
})

export const {authLogin, resetAuthState, updateAuthUser} = auth.actions;

export default auth.reducer