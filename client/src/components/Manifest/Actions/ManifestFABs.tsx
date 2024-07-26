import React, { ReactElement, useContext } from 'react';
import { ManifestEditBtn } from 'src/components/Manifest/Actions/ManifestEditBtn';
import { ManifestSaveBtn } from 'src/components/Manifest/Actions/ManifestSaveBtn';
import { ManifestContext } from 'src/components/Manifest/ManifestForm';
import { QuickSignBtn } from 'src/components/Manifest/QuickerSign';
import { FloatingActionBtn } from 'src/components/UI';
import { useReadOnly } from 'src/hooks/manifest';
import { manifest } from 'src/services';

interface ManifestActionBtnsProps {
  onSignClick: () => void;
}

export function ManifestFABs({ onSignClick }: ManifestActionBtnsProps) {
  const { nextSigningSite, signAble } = useContext(ManifestContext);
  const [readOnly] = useReadOnly();
  const rcraSiteType = manifest.siteTypeToRcraSiteType(nextSigningSite?.siteType);
  let component: ReactElement | undefined = undefined;
  if (!readOnly) {
    component = <ManifestSaveBtn />;
  } else if (signAble) {
    component = <QuickSignBtn siteType={rcraSiteType} onClick={onSignClick} />;
  } else if (readOnly) {
    component = <ManifestEditBtn />;
  } else {
    return <></>;
  }

  return <FloatingActionBtn position="bottom-left" component={component} extended />;
}
