import { HtSpinner } from '~/components/legacyUi';
import React, { createContext, Dispatch, SetStateAction, Suspense, useState } from 'react';
import { Container } from 'react-bootstrap';
import { Outlet } from 'react-router-dom';
import { ErrorBoundary } from '~/components/Error';
import { Sidebar } from './Sidebar/Sidebar';
import { TopNav } from './TopNav/TopNav';

export interface NavContextProps {
  showSidebar: boolean;
  setShowSidebar: Dispatch<SetStateAction<boolean>>;
}

export const NavContext = createContext<NavContextProps>({
  showSidebar: false,
  setShowSidebar: () => console.warn('no showSidebar context'),
});

export function Root() {
  const [showSidebar, setShowSidebar] = useState(false);
  return (
    <NavContext.Provider value={{ showSidebar, setShowSidebar }}>
      <div>
        <TopNav />
        <Sidebar />
        <Container fluid className="tw-mt-20">
          <ErrorBoundary>
            <Suspense fallback={<HtSpinner center className="my-auto" />}>
              <Outlet />
            </Suspense>
          </ErrorBoundary>
        </Container>
      </div>
    </NavContext.Provider>
  );
}
