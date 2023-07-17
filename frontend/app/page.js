"use client";
import { Fragment, useState } from "react";
import { Listbox, Transition } from "@headlessui/react";
import { CheckIcon, ChevronUpDownIcon } from "@heroicons/react/20/solid";
import { useRouter } from "next/navigation";

const categories = [
  {
    id: 1,
    name: "What obligations does this contract place on me ?",
    value: "obligations",
  },
  {
    id: 2,
    name: "How does this contract affect my privacy ?",
    value: "privacy",
  },
  {
    id: 3,
    name: "How does this contract affect my intellectual property rights ?",
    value: "ip",
  },
];

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export default function Home() {
  const [selected, setSelected] = useState(categories[0]);
  const [rawText, setRawText] = useState("");
  const router = useRouter();
  const submit = async (rawText, category) => {
    try {
      const res = await fetch("http://localhost:5000", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          rawText: rawText,
          category: category,
        }),
      });
      console.log("response status");
      console.log(res.status);
      const response = await res.json();
      if (response.success) {
        const info = response.info;
        console.log(info);
        const payload = {
          info,
        };
        sessionStorage.setItem("info", JSON.stringify(payload));
        // router.push("/results");
      } else {
        throw new Error("Something went wrong please try again");
      }
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <main className="min-h-screen p-10">
      <div className="flex flex-col justify-center items-center">
        <h1 className="text-2xl">Find out what you're agreeing to </h1>
        <p className="text-lg"></p>
      </div>

      <div>
        <div className="mb-7">
          <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div className="col-span-full">
              <label className="block text-sm font-medium leading-6 text-gray-900">
                Text
              </label>
              <div className="mt-2">
                <textarea
                  id="about"
                  rows={10}
                  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6 px-3"
                  defaultValue={""}
                  onChange={(e) => setRawText(e.target.value)}
                />
              </div>
              <p className="mt-3 text-sm leading-6 text-gray-600">
                Paste the terms of service agreement in the text area above
              </p>
            </div>
          </div>
        </div>
        <div className="mt-5">
          <Listbox value={selected} onChange={setSelected}>
            {({ open }) => (
              <>
                <Listbox.Label className="block text-sm font-medium leading-6 text-gray-900 mb-3">
                  What do you want to find out ?
                </Listbox.Label>
                <div className="relative">
                  <Listbox.Button className="relative w-full cursor-default rounded-md bg-white py-1.5 pl-3 pr-10 text-left text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 sm:text-sm sm:leading-6">
                    <span className="block truncate">{selected.name}</span>
                    <span className="pointer-events-none absolute inset-y-0 right-0 ml-3 flex items-center pr-2">
                      <ChevronUpDownIcon
                        className="h-5 w-5 text-gray-400"
                        aria-hidden="true"
                      />
                    </span>
                  </Listbox.Button>

                  <Transition
                    show={open}
                    as={Fragment}
                    leave="transition ease-in duration-100"
                    leaveFrom="opacity-100"
                    leaveTo="opacity-0"
                  >
                    <Listbox.Options className="absolute z-10 mt-1 max-h-56 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                      {categories.map((person) => (
                        <Listbox.Option
                          key={person.id}
                          className={({ active }) =>
                            classNames(
                              active
                                ? "bg-indigo-600 text-white"
                                : "text-gray-900",
                              "relative cursor-default select-none py-2 pl-3 pr-9"
                            )
                          }
                          value={person}
                        >
                          {({ selected, active }) => (
                            <>
                              <div className="flex items-center">
                                <span
                                  className={classNames(
                                    selected ? "font-semibold" : "font-normal",
                                    "block truncate"
                                  )}
                                >
                                  {person.name}
                                </span>
                              </div>

                              {selected ? (
                                <span
                                  className={classNames(
                                    active ? "text-white" : "text-indigo-600",
                                    "absolute inset-y-0 right-0 flex items-center pr-4"
                                  )}
                                >
                                  <CheckIcon
                                    className="h-5 w-5"
                                    aria-hidden="true"
                                  />
                                </span>
                              ) : null}
                            </>
                          )}
                        </Listbox.Option>
                      ))}
                    </Listbox.Options>
                  </Transition>
                </div>
              </>
            )}
          </Listbox>
        </div>
      </div>

      <div className="mt-6 flex items-center justify-end gap-x-6">
        <button
          onClick={() => {
            submit(rawText, selected.value);
          }}
          className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Extract
        </button>
      </div>
    </main>
  );
}
